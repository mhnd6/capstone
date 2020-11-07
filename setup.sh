
export DATABASE_PATH='postgres://xvghnwhkvpsmum:9c510ebc2170457c8eac775fa5a7505bc1844ebf3b7450142846152010454a80@ec2-184-73-249-9.compute-1.amazonaws.com:5432/ddfamoh8uvbp4p'

# Flask App config
export FLASK_APP=app
export FLASK_ENV=development

# Configurations gotten from the account created on Auth0
export AUTH0_DOMAIN=mhnd.us.auth0.com
export ALGORITHMS=RS256
export API_AUDIENCE=casting_agency

export AUTH0_CLIENT_ID=2dhpiwOZQ1hUyWfWaztItpn5B0eXic06
export AUTH0_CALLBACK_URL=https://capstone-mhnd.herokuapp.com/