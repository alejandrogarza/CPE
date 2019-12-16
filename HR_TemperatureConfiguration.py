from datetime import datetime

def get_hour_difference(end, start):
  time_difference = datetime.fromisoformat(end) - datetime.fromisoformat(start)
  hour_difference = time_difference.seconds / 3600

  return hour_difference

def calculcate_temperature(from_temperature, hour_difference, to_temperature, speed):
  temperature = from_temperature
  if to_temperature > from_temperature:
    temperature += hour_difference * speed
  elif to_temperature < from_temperature:
    temperature -= hour_difference * speed

  return temperature


def calculate_end_temperature(config):
  initial_temperature = config['initialTemperature']
  current_temperature = initial_temperature
  number_inputs = len(config['inputs'])
  for i in range(number_inputs-1):
    hour_difference = get_hour_difference(config['inputs'][i + 1]['time'], config['inputs'][i]['time'])
    current_temperature = calculcate_temperature(current_temperature, hour_difference, config['inputs'][i]['temperature'], config['speed'])
  
  last_hour_difference = get_hour_difference(config['endTime'], config['inputs'][number_inputs-1]['time'])
  current_temperature = calculcate_temperature(current_temperature, last_hour_difference, config['inputs'][number_inputs-1]['temperature'], config['speed'])

  return current_temperature

  print(config['initialTemperature'], 'inputs: ', number_inputs)


thermostat_config = {"speed":10,"inputs":[{"time":"2016-09-11 11:00","temperature":25},{"time":"2016-09-11 12:00","temperature":35}],"endTime":"2016-09-11 12:30","initialTemperature":15}

print(calculate_end_temperature(thermostat_config))
