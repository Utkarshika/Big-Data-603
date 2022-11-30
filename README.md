
# Tracking the NASA Satellite

For this assignment, we will be working on streaming data which is satellite location coordinates being provided by NASA.

The data is in the following format:
{"timestamp": 1667492679, "iss_position": {"longitude": "-56.8155", "latitude": "-42.5979"}, "message": "success"}

Data can be accessed from http://api.open-notify.org/iss-now.json

The link can be thought of as the producer as it will do producer job.

Write the consumer to connect and fetch data. In the consumer, you have to write the code which takes the data from producer and uses the location coordinates to plot the satellite location on the world map.
The streaming interval should be 5 seconds. The producer should run for an hour. The graph will show the satellite tracking for 1 hr.

P.S.: Keeping in mind that satellite travels very fast, the graph will have more than half of map covered with satellite track
