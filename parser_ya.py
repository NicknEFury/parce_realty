import requests
from realty import check_database


def get_json():
    cookies = {
        'yandexuid': '2705471771671118484',
        'my': '',
        'yandex_gid': '',
        'i': 'bVNQ1TpObObmPNjVyhW8RBmwIj+bA63fdp65TDp0k0DWxAr+ia/E56l8pC8GsgssCs018qZ64vjHLMRjRpc3L95x0n8=',
        'yandex_login': 'peselogo',
        'L': 'SChZCGBDYWBjYFkCDQAJbGJTQ3x3YgpjNQBCUiQ/KCc=.1675281182.15240.318758.33388c32f2be6171a093ee27430138f2',
        'Session_id': '3:1675281183.5.0.1675281182204:wLwSBQ:23.1.2:1|1750472542.-1.2.1:331616988|6:10179527.760385.VQQroS4yr7DvQUH7SZAdx4mEc-8',
        'yp': '1986909622.multib.1#1675885921.szm.1:1920x1080:1920x937#1990641183.udn.cDpwZXNlbG9nbw%3D%3D',
        'mda2_beacon': '1675281183046',
        'suid': '9566aa000a6b16e4ca6cd319d0a5167a.d64cd7eaec275861ccd763ebfe328598',
        'exp_uid': '2a2256e3-1e28-4df5-9a68-6cc52856bf86',
        'font_loaded': 'YSv1',
        'gdpr': '0',
        '_ym_uid': '1693330673840662646',
        '_ym_d': '1693330673',
        'link_to_global_tooltip_shown': 'YES',
        '_csrf_token': '4fd058f84dc72b19835f340ff2b04171e287e123d32ff2a8',
        '_yasc': 'pbgTBez+Gl1PAsYJoPiXNcYw20BqjqM/fifQnLeV5/lAwGmtPuVeZHmjnyoC9Q==',
        'Cookie_check': 'checked',
        'from': 'google-search',
        'prev_uaas_data': '%7B%22uaasUid%22%3A%222705471771671118484%22%2C%22uaasExpNames%22%3A%5B%22REALTYFRONT-16375_cashback_from_yandex_plus_in_card%22%2C%22REALTYFRONT-16113_bring_tenant_banner%22%2C%22REALTYFRONT-16213_change_rent_chat_buttons%22%2C%22REALTYFRONT-16792_show_arenda_chat_button%22%2C%22REALTYFRONT-17278__remove_tenant_fields%22%2C%22REALTYFRONT-17315_create_rent_offer_arenda_trap%22%2C%22REALTYFRONT-17599_new_owner_target%22%2C%22REALTYFRONT-16960-mortgage-calc-on-cards%22%2C%22REALTYFRONT-18136_disable-all-popups%22%2C%22REALTYFRONT-18038_tenant_search_bar%22%2C%22REALTYFRONT-17078_auto_compilation_offers%22%2C%22REALTYFRONT-17031_site_rating%22%2C%22REALTYFRONT-17674_ads_in_card_fs_gallery_on_desktop%22%2C%22REALTYFRONT-18047_owner_flat_draft_form_public%22%2C%22realty_aa_experiment%22%2C%22REALTYFRONT-17334_group_2%22%5D%7D',
        'prev_uaas_expcrypted': '7NXbKZoqbnARcaCmOUU6N8DBvtOXLaq4ewjGJEsTC8gjEHOXii6HMhoDnTPHSn0HU0P_Ysh-byixH3yvWPsrMHlWltPfTi36q5KZezlN505l5TqRX538-e-TjgNGHKPSM0d2ArpyMV1OUAaaSpF_lhBP5WMLzyit',
        '_ym_isad': '2',
        'rgid': '425000',
        'geo_id': '10891',
        'region_id': '10174',
        'from_lifetime': '1693419890608',
    }

    headers = {
        'authority': 'realty.ya.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'client-view-type': 'desktop',
        'cookie': 'yandexuid=2705471771671118484; my=; yandex_gid=; i=bVNQ1TpObObmPNjVyhW8RBmwIj+bA63fdp65TDp0k0DWxAr+ia/E56l8pC8GsgssCs018qZ64vjHLMRjRpc3L95x0n8=; yandex_login=peselogo; L=SChZCGBDYWBjYFkCDQAJbGJTQ3x3YgpjNQBCUiQ/KCc=.1675281182.15240.318758.33388c32f2be6171a093ee27430138f2; Session_id=3:1675281183.5.0.1675281182204:wLwSBQ:23.1.2:1|1750472542.-1.2.1:331616988|6:10179527.760385.VQQroS4yr7DvQUH7SZAdx4mEc-8; yp=1986909622.multib.1#1675885921.szm.1:1920x1080:1920x937#1990641183.udn.cDpwZXNlbG9nbw%3D%3D; mda2_beacon=1675281183046; suid=9566aa000a6b16e4ca6cd319d0a5167a.d64cd7eaec275861ccd763ebfe328598; exp_uid=2a2256e3-1e28-4df5-9a68-6cc52856bf86; font_loaded=YSv1; gdpr=0; _ym_uid=1693330673840662646; _ym_d=1693330673; link_to_global_tooltip_shown=YES; _csrf_token=4fd058f84dc72b19835f340ff2b04171e287e123d32ff2a8; _yasc=pbgTBez+Gl1PAsYJoPiXNcYw20BqjqM/fifQnLeV5/lAwGmtPuVeZHmjnyoC9Q==; Cookie_check=checked; from=google-search; prev_uaas_data=%7B%22uaasUid%22%3A%222705471771671118484%22%2C%22uaasExpNames%22%3A%5B%22REALTYFRONT-16375_cashback_from_yandex_plus_in_card%22%2C%22REALTYFRONT-16113_bring_tenant_banner%22%2C%22REALTYFRONT-16213_change_rent_chat_buttons%22%2C%22REALTYFRONT-16792_show_arenda_chat_button%22%2C%22REALTYFRONT-17278__remove_tenant_fields%22%2C%22REALTYFRONT-17315_create_rent_offer_arenda_trap%22%2C%22REALTYFRONT-17599_new_owner_target%22%2C%22REALTYFRONT-16960-mortgage-calc-on-cards%22%2C%22REALTYFRONT-18136_disable-all-popups%22%2C%22REALTYFRONT-18038_tenant_search_bar%22%2C%22REALTYFRONT-17078_auto_compilation_offers%22%2C%22REALTYFRONT-17031_site_rating%22%2C%22REALTYFRONT-17674_ads_in_card_fs_gallery_on_desktop%22%2C%22REALTYFRONT-18047_owner_flat_draft_form_public%22%2C%22realty_aa_experiment%22%2C%22REALTYFRONT-17334_group_2%22%5D%7D; prev_uaas_expcrypted=7NXbKZoqbnARcaCmOUU6N8DBvtOXLaq4ewjGJEsTC8gjEHOXii6HMhoDnTPHSn0HU0P_Ysh-byixH3yvWPsrMHlWltPfTi36q5KZezlN505l5TqRX538-e-TjgNGHKPSM0d2ArpyMV1OUAaaSpF_lhBP5WMLzyit; _ym_isad=2; rgid=425000; geo_id=10891; region_id=10174; from_lifetime=1693419890608',
        'referer': 'https://realty.ya.ru/sosnovyy_bor/kupit/kommercheskaya-nedvizhimost/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-metrika-client-id': '1693330673840662646',
        'x-requested-with': 'XMLHttpRequest',
        'x-retpath-y': 'https://realty.ya.ru/sosnovyy_bor/kupit/kommercheskaya-nedvizhimost/',
    }

    params = {
        'rgid': '425000',
        'type': 'SELL',
        'category': 'COMMERCIAL',
        'sort': 'DATE_DESC',
        '_pageType': 'search',
        '_providers': [
            'seo',
            'queryId',
            'forms',
            'filters',
            'filtersParams',
            'mapsPromo',
            'newbuildingPromo',
            'refinements',
            'search',
            'react-search-data',
            'searchHistoryParams',
            'searchParams',
            'searchPresets',
            'showSurveyBanner',
            'seo-data-offers-count',
            'related-newbuildings',
            'breadcrumbs',
            'ads',
            'mf-footer',
            'offers-stats',
            'seo-texts',
            'samolet-plus-serp-snippets',
            'ya-arenda-rent-pladge-snippets',
            'init-ya-arenda-slider-snippets',
            'reviews',
        ],
        'crc': 'ydc502b2bc23a77849756016b7d11207b',
    }

    response = requests.get('https://realty.ya.ru/gate/react-page/get/', params=params, cookies=cookies,
                            headers=headers)
    data = response.json()

    return data


def get_offer(item):
    offer = {}

    offer["url"] = item["shareUrl"]
    offer["offer_id"] = item["offerId"]

    if item.get("updateDate"):
        offer_date = item["updateDate"].replace('T', ' ').replace('Z', '')
    else:
        offer_date = item["creationDate"].replace('T', ' ').replace('Z', '')
    offer["date"] = offer_date

    offer["price"] = item["price"]["value"]
    offer["address"] = item["location"]["address"]
    offer["area"] = item["area"]["value"]
    offer["rooms"] = item["roomsTotalKey"]
    offer["floor"] = item["floorsOffered"][0]
    offer["total_floor"] = item["floorsTotal"]

    return offer


def get_offers(data):
    entities = data["response"]["search"]["offers"]["entities"]
    for item in entities:
        offer = get_offer(item)
        check_database(offer)

def main():
    data = get_json()
    print(data)
    #get_offers(data)


if __name__ == '__main__':
    main()