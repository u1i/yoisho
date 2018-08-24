curl -X POST \
  http://localhost:8080/atm/locations \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: e283f4e9-0766-49e9-b22e-d2524b0249ef' \
  -d '{"lat": "33333", "lon": "09393", "location": "some place"}'
