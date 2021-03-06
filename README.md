# Validation/staking rewards

This is a simple web server that calculates monthly rewards for Polkadot, Kusama and various parachains. 

## Installation

There is currently no `pip` package for this project. Therefore you need to clone it from this repo and install dependencies
yourself

```
git clone https://github.com/polkadotters/polkadot-reward-calculator.git
pip install flask
pip install flask-restx
pip install requests
```

## Usage

Usage is pretty straightforward, you need to specify the network and the address 

```
curl 127.0.0.1:5000/rewards?network=kilt&address=4pnAJ41mGHGDKCGBGY2zzu1hfvPasPkGAKDgPeprSkxnUmGM
```

There are only two parameters right now
 - `address`
 - `network`

### Supported networks
- Polkadot
- Kusama
- Kilt
- Moonbeam
- Moonriver
- Astar

There's also a simple error checking which verifies that both parameters are present and network is supported.

## Authentication

Authentication is done simply via `X-API-KEY` header which has to be present in all requests. In order to set this key
on the sever, you need to export `REWARDS_API_KEY` variable that will represent this authentication key for the clients.

You also need to export `SUBSCAN_API_KEY` that is needed in order to access Subscan API.
