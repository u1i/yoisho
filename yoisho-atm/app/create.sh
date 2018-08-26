curl -X POST \
  http://localhost:8080/api/atm \
  -d "{\"lat\": \"${RANDOM}${RANDOM}\", \"lon\": \"${RANDOM}${RANDOM}\", \"location\": \"some place\"}"
