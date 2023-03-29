import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set some variables
api_key = '<mTI-I2dBG8ijfvXDzhigJ7uHS3z4N7Hh0S8q7v_5-CR6>'
api_url = '<https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/68cff5a8-59b3-43b1-bf41-20cb6747d4e0>'
model_id = 'en-it'
text_to_translate = 'Your content you want translate here'

# Prepare the Authenticator
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(api_url )

# Translate
translation = language_translator.translate(
    text=text_to_translate,
    model_id=model_id).get_result()

# Print results
print(json.dumps(translation, indent=2, ensure_ascii=False))