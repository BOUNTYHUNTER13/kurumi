from aiohttp import ClientSession
from Python_ARQ import ARQ

aiohttpsession = ClientSession()

arq = ARQ("https://thearq.tech", "HJFBTG-USOQTO-MVVAFB-XRRVPJ-ARQ", aiohttpsession)
