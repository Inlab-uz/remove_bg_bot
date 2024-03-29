import requests

# url = "https://background-removal.p.rapidapi.com/remove"
#
# headers = {
#     'content-type': "application/x-www-form-urlencoded",
#     'x-rapidapi-host': "background-removal.p.rapidapi.com",
#     'x-rapidapi-key': "16385339c4msh71817e244897c09p1a5a57jsnc80d7d497e4b"
#     }
# # test payload
# # payload = "image_url=https%3A%2F%2Fobjectcut.com%2Fassets%2Fimg%2Fraven.jpg"
#
# async def remove_background(img_url):
#     payload = f"image_url={img_url}"
#     response = requests.request("POST", url, data=payload, headers=headers)
#     # logging.info(response.json()['response']['image_url'])
#     # return response.text
#     return response.json()['response']['image_url']


async def remove_background(img_url):
    # response = requests.post(
    #     'https://api.remove.bg/v1.0/removebg',
    #     files={'image_file': f'{img_url}'},
    #     data={'size': 'auto'},
    #     headers={'X-Api-Key': 'HCoZeA5GQZxYeKSrg9ThCSQt'},
    # )
    # if response.status_code == requests.codes.ok:
    #     return response.content
    #         # out.write(response.content)
    # else:iiQi1iEVTuFHaM374bTK5KT3
    #     return "Error: {response.status_code, response.text}"

    response = requests.post(
        'https://sdk.photoroom.com/v1/segment',
        headers={'x-api-key': '1e352e0fb19099fe2984cdc43d90614da96d1840'},
        files={'image_file': open(f'{img_url}', 'rb')},
    )

    response.raise_for_status()
    with open(f'{img_url}', 'wb') as f:
        f.write(response.content)
