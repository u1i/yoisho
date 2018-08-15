# The URL of the oauth server - routable through the browser
export oauth_url="http://localhost:8091"

# The URL of the oauth server - routable from within the app container
export oauth_url_serverside="http://172.17.0.1:8091"

# The app URL
export app_url="http://localhost:8050"

docker run -d -p 8050:8080 -e oauth_url=$oauth_url -e oauth_url_serverside=$oauth_url_serverside -e app_port=$app_port -e app_url=$app_url u1ih/yoisho-account-oauth-client
