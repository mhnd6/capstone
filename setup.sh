
export DATABASE_PATH='postgres://kfnfjvoufgjsms:d06cc6e2c21a15a290580c83f7421cdf9738e37e2f3f59af5d3c3a6c254a6da0@ec2-54-224-124-241.compute-1.amazonaws.com:5432/daec96hp8b5qo3'

# Flask App config
export FLASK_APP=app
export FLASK_ENV=development

# Configurations gotten from the account created on Auth0
export AUTH0_DOMAIN=mhnd.us.auth0.com
export ALGORITHMS=RS256
export API_AUDIENCE=casting_agency

export AUTH0_CLIENT_ID=2dhpiwOZQ1hUyWfWaztItpn5B0eXic06
export AUTH0_CALLBACK_URL=https://capstone-mhnd.herokuapp.com/