
def downloadSurvey():
    import requests
    import zipfile
    import shutil, os

    request = requests.get("https://drive.google.com/uc?export=download&id=1_9On2-nsBQIw3JiY43sWbrF8EjrqrR4U")
    with open("survey2018.zip", "wb") as file:
        file.write(request.content)

    with zipfile.ZipFile('survey2018.zip') as zip:
        zip.extractall('survey2018')

    shutil.move('survey2018/survey_results_public.csv', 'survey.csv')
    shutil.rmtree('survey2018')
    os.remove('survey2018.zip')

downloadSurvey()
