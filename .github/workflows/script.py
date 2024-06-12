import requests

def download_file_from_google_drive(file_url, destination_path):
    session = requests.Session()

    response = session.get(file_url, stream=True)
    token = None

    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            token = value

    if token:
        params = {'id': file_url.split('/')[-2], 'confirm': token}
        response = session.get('https://drive.google.com/uc', params=params, stream=True)

    with open(destination_path, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)

file_url = "https://drive.google.com/drive/folders/10Z0R_I-ptN2h5uFPwK_T1MOpVPLj8Qea?usp=drive_link"
destination_path = "downloaded_update.zip"

download_file_from_google_drive(file_url, destination_path)
print("Update downloaded successfully!")
