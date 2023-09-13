from datetime import datetime
import requests
from realty import check_database


def get_offer(item):
    offer = {}

    offer["url"] = item["fullUrl"]
    offer["offer_id"] = item["id"]

    timestamp = datetime.fromtimestamp(item["addedTimestamp"])
    timestamp = datetime.strftime(timestamp, '%Y-%m-%d %H:%M:%S')
    offer["date"] = timestamp

    offer["price"] = item["bargainTerms"]["priceRur"]
    offer["address"] = item["geo"]["userInput"]
    offer["area"] = item["totalArea"]
    offer["rooms"] = item["roomsCount"]
    offer["floor"] = item["floorNumber"]
    offer["total_floor"] = item["building"]["floorsCount"]

    return offer


def get_offers(data):
    for item in data["data"]["offersSerialized"]:
        offer = get_offer(item)
        check_database(offer)


def get_json():
    cookies = {
        '_CIAN_GK': '1cba2302-cc41-479b-8935-8d03d9ac80a3',
        '_gcl_au': '1.1.1254668330.1693329098',
        'tmr_lvid': 'c82ece9b2b62b906f77e5cd5d714c462',
        'tmr_lvidTS': '1693329098451',
        'cookie_agreement_accepted': '1',
        'sopr_utm': '%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D',
        'uxfb_usertype': 'searcher',
        '_ym_uid': '1693329140984719847',
        '_ym_d': '1693329140',
        '_gid': 'GA1.2.662553030.1693329140',
        'uxs_uid': '368b23a0-468f-11ee-bb62-9930d39db14f',
        'afUserId': '6d62ccb1-5771-4d08-b378-8aeefe47ef10-p',
        'adrcid': 'AK4nQq_gh1tZQUmEngt00AQ',
        'AF_SYNC': '1693394438015',
        'login_mro_popup': '1',
        '_ym_isad': '2',
        'session_region_id': '1',
        'session_main_town_region_id': '1',
        'serp_registration_trigger_popup': '1',
        'sopr_session': '494a45a7bda4448f',
        '__cf_bm': '_FfO_9WTnE.zRmbtYVASQXejZUwBA.tAzl.7345kSGs-1693421013-0-AdN2jh2OAzYQJjEtR5KpVAtJW8qmeVrUCMGFPIwYgpEkYLqSwV0xRXOd6GE7YH3EV2im/4YyR/wnf46y/2OaFec=',
        '_ym_visorc': 'b',
        'viewpageTimer': '3866.9249999999997',
        '_ga': 'GA1.2.240490562.1693329140',
        '_ga_3369S417EL': 'GS1.1.1693419150.4.1.1693421322.45.0.0',
        '_dc_gtm_UA-30374201-1': '1',
    }

    headers = {
        'authority': 'api.cian.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': '_CIAN_GK=1cba2302-cc41-479b-8935-8d03d9ac80a3; _gcl_au=1.1.1254668330.1693329098; tmr_lvid=c82ece9b2b62b906f77e5cd5d714c462; tmr_lvidTS=1693329098451; cookie_agreement_accepted=1; sopr_utm=%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D; uxfb_usertype=searcher; _ym_uid=1693329140984719847; _ym_d=1693329140; _gid=GA1.2.662553030.1693329140; uxs_uid=368b23a0-468f-11ee-bb62-9930d39db14f; afUserId=6d62ccb1-5771-4d08-b378-8aeefe47ef10-p; adrcid=AK4nQq_gh1tZQUmEngt00AQ; AF_SYNC=1693394438015; login_mro_popup=1; _ym_isad=2; session_region_id=1; session_main_town_region_id=1; serp_registration_trigger_popup=1; sopr_session=494a45a7bda4448f; __cf_bm=_FfO_9WTnE.zRmbtYVASQXejZUwBA.tAzl.7345kSGs-1693421013-0-AdN2jh2OAzYQJjEtR5KpVAtJW8qmeVrUCMGFPIwYgpEkYLqSwV0xRXOd6GE7YH3EV2im/4YyR/wnf46y/2OaFec=; _ym_visorc=b; viewpageTimer=3866.9249999999997; _ga=GA1.2.240490562.1693329140; _ga_3369S417EL=GS1.1.1693419150.4.1.1693421322.45.0.0; _dc_gtm_UA-30374201-1=1',
        'origin': 'https://www.cian.ru',
        'referer': 'https://www.cian.ru/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    json_data = {
        'jsonQuery': {
            '_type': 'commercialsale',
            'engine_version': {
                'type': 'term',
                'value': 2,
            },
            'office_type': {
                'type': 'terms',
                'value': [
                    12,
                    11,
                    9,
                    7,
                    4,
                    5,
                    3,
                    2,
                    1,
                    10,
                ],
            },
            'region': {
                'type': 'terms',
                'value': [
                    1,
                ],
            },
            'ready_business_types': {
                'type': 'terms',
                'value': [
                    2,
                    1,
                ],
            },
            'sort': {
                'type': 'term',
                'value': 'creation_date_desc',
            },
        },
    }

    response = requests.post(
        'https://api.cian.ru/commercial-search-offers/desktop/v1/offers/get-offers/',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    result = response.json()
    return result


def main():
    data = get_json()
    print(data)
    #get_offers(data)


if __name__ == '__main__':
    main()