import datetime
import os
import shutil
import zipfile
from xml.etree.ElementTree import iterparse

import numpy as np
import pandas as pd
import requests

from core.models import Organization
from core.services.roszdrav.headers import HEADERS, FIELDS_LIST


def format_date(date_str=None):
    if date_str:
        return datetime.datetime.strptime(date_str, "%d.%m.%Y").strftime("%Y-%m-%d")
    return None


class ImportData:

    def __init__(self):
        self.base_url = 'https://roszdravnadzor.gov.ru/opendata/7710537160-med_licenses/'
        self.cookies = self._get_cookies()

    def _get_cookies(self):
        resp = requests.get('https://roszdravnadzor.gov.ru/opendata/7710537160-med_licenses/',
                            headers=HEADERS,
                            timeout=60)
        if resp.status_code == '200':
            return resp.cookies
        return None

    def _get_actual_file(self):
        resp = requests.get('https://roszdravnadzor.gov.ru/opendata/7710537160-med_licenses/meta.csv',
                            headers=HEADERS,
                            timeout=60,
                            cookies=self.cookies)
        resp.encoding = resp.apparent_encoding

        for line in resp.text.splitlines():
            if line.startswith('data'):
                url = line.split(',')[1]
                break
        return url

    def _save_and_extract(self):
        url = self._get_actual_file()
        resp = requests.get(
            url,
            headers=HEADERS,
            timeout=60,
            cookies=self.cookies)

        if os.path.exists('temp/'):
            shutil.rmtree('temp/')
        os.mkdir('temp/')
        with open('temp/temp.zip', 'wb') as file:
            file.write(resp.content)
        with zipfile.ZipFile('temp/temp.zip', 'r') as zip_ref:
            zip_ref.extractall('temp/')
        os.remove('temp/temp.zip')

    def parse(self):
        self._save_and_extract()

        for file in os.listdir('temp/'):
            file_path = 'temp/' + file
            break

        dict_list = []
        for event, elem in iterparse(file_path, events=['start']):

            if elem.tag == 'licenses':
                my_dict = {}
                for child in elem.iter():
                    if child.tag in FIELDS_LIST:
                        my_dict[child.tag] = child.text
                if my_dict.get('name'):
                    dict_list.append(my_dict)

            elem.clear()

        df = pd.DataFrame(dict_list).replace({np.nan: None})

        new_orgs = []
        for _, row in df.iterrows():
            new_orgs.append(Organization(
                name=row['name'],
                activity_type=row['activity_type'],
                address_region=row['address_region'],
                full_name_licensee=row['full_name_licensee'],
                address=row['address'],
                ogrn=row['ogrn'],
                inn=row['inn'],
                number=row['number'],
                date=format_date(row['date'])
            ))
        Organization.objects.bulk_create(new_orgs, batch_size=10000)


# if __name__ == '__main__':
#     idata = ImportData()
#     idata.parse()
