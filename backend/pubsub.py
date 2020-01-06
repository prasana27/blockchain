from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'sub-c-b1deee10-2ffa-11ea-aaf2-c6d8f98a95a1'
pnconfig.publish_key = 'pub-c-3f8a8431-a839-4a8d-8152-b0be0862e684'

pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

def main():
    pubnub.publish().channel(TEST_CHANNEL).message({'PK':'GOAT'}).sync()

if __name__ == '__main__':
    main()