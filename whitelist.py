"""The whitelist contains list of exchanges that are accessed by the aggregator to collect OHLCV
data (all other supported by ccxt are ignored). Each exchange has a corresponding list of pairs
that we want to poll. If the list is empty, we want to poll all available pairs' OHLCV data."""
whitelist = {'exchanges': {
                          'binance': [],
                          'bitz': ['LTC/BTC', 'ETH/BTC', 'ZEC/BTC', 'LSK/BTC', 'BCH/BTC', 'QTUM/BTC', 'GAME/BTC', 'TRX/BTC', 'ETC/BTC', 'HSR/BTC', 'NULS/BTC', 'EOS/BTC', 'PPC/BTC'],
                          'cobinhood': ['STK/BTC', 'TRX/BTC', 'TRX/ETH', 'STK/ETH', 'VOISE/BTC', 'VOISE/ETH', 'FUN/ETH', 'DRGN/BTC', 'DRGN/ETH', 'ZRX/BTC', 'ETH/BTC', 'COB/BTC', 'NGC/BTC', 'NGC/ETH', 'OMG/ETH', 'UTNP/BTC', 'COB/ETH', 'CMT/BTC', 'CMT/ETH', 'SPHTX/BTC', 'SPHTX/ETH', 'UTNP/ETH', 'BDG/BTC', 'BDG/ETH', 'EOS/BTC', 'PAY/BTC', 'ENJ/BTC', 'ENJ/ETH', 'PAY/ETH', 'EOS/ETH', 'BAT/BTC', 'BAT/ETH', 'GTC/BTC', 'GTC/ETH', 'IOST/ETH', 'ETHOS/BTC', 'CVC/ETH', 'OCN/BTC', 'OCN/ETH', 'ETHOS/ETH'],
                          'hitbtc2': ['BTC/USDT', 'ETH/BTC', 'LTC/USDT', 'XDN/BTC', 'ARDR/BTC', 'MAID/BTC', 'DASH/USDT', 'ETH/USDT', 'NXT/USDT', 'ZEC/USDT', 'XEM/USDT', 'XDN/USDT', 'MAID/USDT', 'XMR/ETH', 'ETC/ETH', 'DASH/ETH', 'ZEC/ETH', 'NET/ETH', 'ADX/ETH', 'XTZ/ETH', 'SUR/ETH', 'STX/USDT', 'BCH/ETH', 'BCH/USDT', 'ZRX/ETH', 'ZRX/USDT', 'PPC/USDT', 'BMC/USDT', 'AIR/USDT', 'NEO/USDT', 'VIB/USDT', 'EMC/USDT'],
                          'kraken': ['BCH/EUR', 'BCH/USD', 'DASH/EUR', 'EOS/ETH', 'ETC/EUR', 'ETH/BTC', 'ETH/EUR', 'ETH/USD', 'LTC/EUR', 'LTC/USD', 'REP/EUR', 'BTC/EUR', 'BTC/USD', 'XMR/EUR', 'XRP/EUR', 'XRP/USD', 'ZEC/EUR'],
                          'kucoin': [],
                          'okex': ['LTC/BTC', 'ETH/BTC', 'ETC/BTC', 'BCH/BTC', 'XRP/BTC', 'XEM/BTC', 'XLM/BTC', 'IOTA/BTC', '1ST/BTC', 'AAC/BTC', 'ACE/BTC', 'ACT/BTC', 'AIDOC/BTC', 'AMM/BTC', 'ARK/BTC', 'AST/BTC', 'ATL/BTC', 'AVT/BTC', 'BCD/BTC', 'BCS/BTC', 'BCX/BTC', 'BNT/BTC', 'BRD/BTC', 'BT1/BTC', 'BT2/BTC', 'BTG/BTC', 'BTM/BTC', 'CAG/BTC', 'CAN/BTC', 'CBT/BTC', 'CHAT/BTC', 'CIC/BTC', 'CMT/BTC', 'CTR/BTC', 'CVC/BTC', 'DASH/BTC', 'DAT/BTC', 'DENT/BTC', 'DGB/BTC', 'DGD/BTC', 'DNA/BTC', 'DNT/BTC', 'DPY/BTC', 'EDO/BTC', 'ELF/BTC', 'ENG/BTC', 'EOS/BTC', 'EVX/BTC', 'FairGame/BTC', 'FUN/BTC', 'GAS/BTC', 'GNT/BTC', 'GNX/BTC', 'GTO/BTC', 'HMC/BTC', 'HOT/BTC', 'HSR/BTC', 'ICN/BTC', 'ICX/BTC', 'INS/BTC', 'INSUR/BTC', 'INT/BTC', 'IOST/BTC', 'IPC/BTC', 'ITC/BTC', 'KCASH/BTC', 'KEY/BTC', 'KNC/BTC', 'LA/BTC', 'LEND/BTC', 'LEV/BTC', 'LIGHT/BTC', 'LINK/BTC', 'LRC/BTC', 'MAG/BTC', 'MANA/BTC', 'MCO/BTC', 'MDA/BTC', 'MDT/BTC', 'MKR/BTC', 'MOF/BTC', 'MOT/BTC', 'MTH/BTC', 'MTL/BTC', 'NAS/BTC', 'NEO/BTC', 'NGC/BTC', 'NULS/BTC', 'OAX/BTC', 'OF/BTC', 'OMG/BTC', 'OST/BTC', 'PAY/BTC', 'POE/BTC', 'PPT/BTC', 'PRA/BTC', 'PST/BTC', 'QTUM/BTC', 'QUN/BTC', 'QVT/BTC', 'R/BTC', 'RCN/BTC', 'RCT/BTC', 'RDN/BTC', 'READ/BTC', 'REF/BTC', 'REQ/BTC', 'RNT/BTC', 'SALT/BTC', 'SAN/BTC', 'SBTC/BTC', 'SHOW/BTC', 'SMT/BTC', 'SNC/BTC', 'SNGLS/BTC', 'SNM/BTC', 'SNT/BTC', 'SOC/BTC', 'SPF/BTC', 'SSC/BTC', 'STC/BTC', 'STORJ/BTC', 'SUB/BTC', 'SWFTC/BTC', 'TCT/BTC', 'THETA/BTC', 'TIO/BTC', 'TNB/BTC', 'TOPC/BTC', 'TRUE/BTC', 'TRX/BTC', 'UBTC/BTC', 'UCT/BTC', 'UGC/BTC', 'UKG/BTC', 'UTK/BTC', 'VEE/BTC', 'VIB/BTC', 'VIU/BTC', 'WBTC/BTC', 'WRC/BTC', 'WTC/BTC', 'XMR/BTC', 'XUC/BTC', 'YEE/BTC', 'ZEC/BTC', 'ZEN/BTC', 'ZIP/BTC', 'ZRX/BTC', 'BTC/USDT', 'BTC/USD', 'LTC/USDT', 'LTC/USD', 'ETH/USDT', 'ETH/USD', 'ETC/USDT', 'ETC/USD', 'BCH/USDT', 'BCH/USD', 'XRP/USDT', 'XRP/USD', 'XEM/USDT', 'XLM/USDT', 'IOTA/USDT', '1ST/USDT', 'AAC/USDT', 'ACE/USDT', 'ACT/USDT', 'AIDOC/USDT', 'AMM/USDT', 'ARK/USDT', 'AST/USDT', 'ATL/USDT', 'AVT/USDT', 'BCD/USDT', 'BNT/USDT', 'BRD/USDT', 'BTG/USDT', 'BTG/USD', 'BTM/USDT', 'CAG/USDT', 'CAN/USDT', 'CBT/USDT', 'CHAT/USDT', 'CIC/USDT', 'CMT/USDT', 'CTR/USDT', 'CVC/USDT', 'DASH/USDT', 'DAT/USDT', 'DENT/USDT', 'DGB/USDT', 'DGD/USDT', 'DNA/USDT', 'DNT/USDT', 'DPY/USDT', 'EDO/USDT', 'ELF/USDT', 'ENG/USDT', 'EOS/USDT', 'EOS/USD', 'EVX/USDT', 'FairGame/USDT', 'FUN/USDT', 'GAS/USDT', 'GNT/USDT', 'GNX/USDT', 'GTO/USDT', 'HMC/USDT', 'HOT/USDT', 'HSR/USDT', 'ICN/USDT', 'ICX/USDT', 'INS/USDT', 'INSUR/USDT', 'INT/USDT', 'IOST/USDT', 'IPC/USDT', 'ITC/USDT', 'KCASH/USDT', 'KEY/USDT', 'KNC/USDT', 'LA/USDT', 'LEND/USDT', 'LEV/USDT', 'LIGHT/USDT', 'LINK/USDT', 'LRC/USDT', 'MAG/USDT', 'MANA/USDT', 'MCO/USDT', 'MDA/USDT', 'MDT/USDT', 'MKR/USDT', 'MOF/USDT', 'MOT/USDT', 'MTH/USDT', 'MTL/USDT', 'NAS/USDT', 'NEO/USDT', 'NGC/USDT', 'NULS/USDT', 'OAX/USDT', 'OF/USDT', 'OMG/USDT', 'OST/USDT', 'PAY/USDT', 'POE/USDT', 'PPT/USDT', 'PRA/USDT', 'PST/USDT', 'QTUM/USDT', 'QUN/USDT', 'QVT/USDT', 'R/USDT', 'RCN/USDT', 'RCT/USDT', 'RDN/USDT', 'READ/USDT', 'REF/USDT', 'REQ/USDT', 'RNT/USDT', 'SALT/USDT', 'SAN/USDT', 'SHOW/USDT', 'SMT/USDT', 'SNC/USDT', 'SNGLS/USDT', 'SNM/USDT', 'SNT/USDT', 'SOC/USDT', 'SPF/USDT', 'SSC/USDT', 'STC/USDT', 'STORJ/USDT', 'SUB/USDT', 'SWFTC/USDT', 'TCT/USDT', 'THETA/USDT', 'TIO/USDT', 'TNB/USDT', 'TOPC/USDT', 'TRUE/USDT', 'TRX/USDT', 'UBTC/USDT', 'UCT/USDT', 'UGC/USDT', 'UKG/USDT', 'UTK/USDT', 'VEE/USDT', 'VIB/USDT', 'VIU/USDT', 'WRC/USDT', 'WTC/USDT', 'XMR/USDT', 'XUC/USDT', 'YEE/USDT', 'ZEC/USDT', 'ZEN/USDT', 'ZIP/USDT', 'ZRX/USDT', 'LTC/BCH', 'ETC/BCH', 'ACT/BCH', 'AVT/BCH', 'BCD/BCH', 'BCX/BCH', 'BTG/BCH', 'CMT/BCH', 'DASH/BCH', 'DGD/BCH', 'EDO/BCH', 'EOS/BCH', 'SBTC/BCH', 'LTC/ETH', 'ETC/ETH', 'BCH/ETH', 'XRP/ETH', 'XEM/ETH', 'XLM/ETH', 'IOTA/ETH', '1ST/ETH', 'AAC/ETH', 'ACE/ETH', 'ACT/ETH', 'AIDOC/ETH', 'AMM/ETH', 'ARK/ETH', 'AST/ETH', 'ATL/ETH', 'AVT/ETH', 'BNT/ETH', 'BRD/ETH', 'BTM/ETH', 'CAG/ETH', 'CAN/ETH', 'CBT/ETH', 'CHAT/ETH', 'CIC/ETH', 'CMT/ETH', 'CTR/ETH', 'CVC/ETH', 'DASH/ETH', 'DAT/ETH', 'DENT/ETH', 'DGB/ETH', 'DGD/ETH', 'DNA/ETH', 'DNT/ETH', 'DPY/ETH', 'EDO/ETH', 'ELF/ETH', 'ENG/ETH', 'EOS/ETH', 'EVX/ETH', 'FairGame/ETH', 'FUN/ETH', 'GAS/ETH', 'GNT/ETH', 'GNX/ETH', 'GTO/ETH', 'HMC/ETH', 'HOT/ETH', 'HSR/ETH', 'ICN/ETH', 'ICX/ETH', 'INS/ETH', 'INSUR/ETH', 'INT/ETH', 'IOST/ETH', 'IPC/ETH', 'ITC/ETH', 'KCASH/ETH', 'KEY/ETH', 'KNC/ETH', 'LA/ETH', 'LEND/ETH', 'LEV/ETH', 'LIGHT/ETH', 'LINK/ETH', 'LRC/ETH', 'MAG/ETH', 'MANA/ETH', 'MCO/ETH', 'MDA/ETH', 'MDT/ETH', 'MKR/ETH', 'MOF/ETH', 'MOT/ETH', 'MTH/ETH', 'MTL/ETH', 'NAS/ETH', 'NEO/ETH', 'NGC/ETH', 'NULS/ETH', 'OAX/ETH', 'OF/ETH', 'OMG/ETH', 'OST/ETH', 'PAY/ETH', 'POE/ETH', 'PPT/ETH', 'PRA/ETH', 'PST/ETH', 'QTUM/ETH', 'QUN/ETH', 'QVT/ETH', 'R/ETH', 'RCN/ETH', 'RCT/ETH', 'RDN/ETH', 'READ/ETH', 'REF/ETH', 'REQ/ETH', 'RNT/ETH', 'SALT/ETH', 'SAN/ETH', 'SHOW/ETH', 'SMT/ETH', 'SNC/ETH', 'SNGLS/ETH', 'SNM/ETH', 'SNT/ETH', 'SOC/ETH', 'SPF/ETH', 'SSC/ETH', 'STC/ETH', 'STORJ/ETH', 'SUB/ETH', 'SWFTC/ETH', 'TCT/ETH', 'THETA/ETH', 'TIO/ETH', 'TNB/ETH', 'TOPC/ETH', 'TRUE/ETH', 'TRX/ETH', 'UBTC/ETH', 'UCT/ETH', 'UGC/ETH', 'UKG/ETH', 'UTK/ETH', 'VEE/ETH', 'VIB/ETH', 'VIU/ETH', 'WRC/ETH', 'WTC/ETH', 'XMR/ETH', 'XUC/ETH', 'YEE/ETH', 'ZEC/ETH', 'ZEN/ETH', 'ZIP/ETH', 'ZRX/ETH']
                          }
            }
