old_to_new_map = {
    'oxtest_for':           'oxtest-for',
    'oxtest_cmp':           'oxtest-cmp',
    'oxtest_auction':       'oxtest-auction',
    'oxtest_mobile':        'oxtest-mobile',
    'oxtest_smoke':         'oxtest-smoke',
    'oxtest_aq':            'oxtest-aq',
    'oxtest_ote':           'oxtest-ote',
    'oxtest_angular_ui' :   'oxtest-angular-ui',
    'oxtest_dfp':           'oxtest-dfp',
    'oxtest_video':         'oxtest-video',
    'oxtest_events':        'oxtest-events',
    'oxtest_bidder_ss':     'oxtest-bidder-ss',
    'oxtest_tq':            'oxtest-tq',
    'oxtest_unity_etl':     'oxtest-unity-etl',
    'github-crawler':       'qa-github-crawler'

}

with open('gocd_xml.xml') as file:
    everything = file.read()
    for old_name in old_to_new_map:
        everything = everything.replace(old_name, old_to_new_map[old_name])

with open('gocd_xml.xml','w') as file:
    file.write(everything)