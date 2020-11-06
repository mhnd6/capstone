
export DATABASE_PATH='postgres://postgres:admin@localhost:5432/capstone'

# Flask App config
export FLASK_APP=app
export FLASK_ENV=development

# Configurations gotten from the account created on Auth0
export AUTH0_DOMAIN=mhnd.us.auth0.com
export ALGORITHMS=RS256
export API_AUDIENCE=casting_agency

export AUTH0_CLIENT_ID=2dhpiwOZQ1hUyWfWaztItpn5B0eXic06
export AUTH0_CALLBACK_URL=https://capstone-mhnd.herokuapp.com/