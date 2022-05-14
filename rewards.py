from chains.polkadot import Polkadot
from chains.kusama import Kusama
from chains.moonbeam import Moonbeam
from chains.astar import Astar
from chains.moonriver import Moonriver
from chains.kilt import Kilt

if __name__ == "__main__":
    chain = Kilt()
    print(chain.get_rewards("4pnAJ41mGHGDKCGBGY2zzu1hfvPasPkGAKDgPeprSkxnUmGM"))


