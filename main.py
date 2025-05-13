from exa_py import Exa

exa = Exa('a3fd55f8-9e77-45d7-a584-7e7f0d184e2d')

print('''
   _____ __                         _          _____                      __       ______            _          
  / ___// /_  __  ______ _____ ___ ( )_____   / ___/___  ____ ___________/ /_     / ____/___  ____ _(_)___  ___ 
  \__ \/ __ \/ / / / __ `/ __ `__ \|// ___/   \__ \/ _ \/ __ `/ ___/ ___/ __ \   / __/ / __ \/ __ `/ / __ \/ _ \
 ___/ / / / / /_/ / /_/ / / / / / / (__  )   ___/ /  __/ /_/ / /  / /__/ / / /  / /___/ / / / /_/ / / / / /  __/
/____/_/ /_/\__, /\__,_/_/ /_/ /_/ /____/   /____/\___/\__,_/_/   \___/_/ /_/  /_____/_/ /_/\__, /_/_/ /_/\___/ 
           /____/                                                                          /____/               
''')
print("Your one stop solution for Querying! Backed by Priyanka , Exa AI APIs and LLMs!")

query = input('Search here: ')

response = exa.search(
    query,
    num_results = 5,
    type='keyword',
    include_domains=['https://www.instagram.com'],
)

for results in response.results:
    print(f'Title: {results.title}')
    print(f'URL: {results.url}')
    print()

