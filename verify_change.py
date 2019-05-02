old_ent = [
    'oxtest_for',
    'oxtest_cmp',
    'oxtest_auction',
    'oxtest_mobile',
    'oxtest_smoke',
    'oxtest_aq',
    'oxtest_ote',
    'oxtest_angular_ui',
    'oxtest_dfp',
    'oxtest_video',
    'oxtest_events',
    'oxtest_bidder_ss',
    'oxtest_tq',
    'oxtest_unity_etl',
    'github-crawler']

with open('gocd_xml.xml') as file:
    everything = file.read()
    for i in old_ent:
        if i in everything:
            raise Exception('old name exists')

