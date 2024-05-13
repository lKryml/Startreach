import os
from models import AppConfigModel
from os.path import abspath
from dotenv import load_dotenv
dotenv_path = abspath('../.env')
load_dotenv(dotenv_path=dotenv_path)

url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')

__app_config = AppConfigModel(
    app_description=os.environ.get('APP_DESCRIPTION') if os.environ.get('APP_DESCRIPTION') is not None else 'no descrption',
    app_name=os.environ.get('APP_NAME'),
    app_version=os.environ.get('APP_VERSION', '0.0.0'),
    port=int(os.environ.get('PORT')) if os.environ.get('PORT') is not None and os.environ.get('PORT').isnumeric() else 1337,
    enviroment=os.environ.get('PYTHON_ENVIRONMENT', 'development'),
    is_debug=os.environ.get('PYTHON_ENVIRONMENT') in ('development', 'test'),

    supabase_url=url,
    supabase_key=key
)

app_config = __app_config.model_dump()