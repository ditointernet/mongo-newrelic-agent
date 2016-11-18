import os
import yaml

def generate_agent_config():
    agent_config = {
        'Application': {
            'license_key': os.environ['MONGO_NEWRELIC_AGENT_LICENSE_KEY'],
            'poll_interval': 60,

            'mongodb': {
                'name': os.environ['MONGO_NEWRELIC_AGENT_NAME'],
                'host': os.environ['MONGO_NEWRELIC_AGENT_HOST'],
                'port': int(os.environ['MONGO_NEWRELIC_AGENT_PORT']),
                'databases': os.environ['MONGO_NEWRELIC_AGENT_DATABASES'].split(',')
            }
        }
    }

    return agent_config

if __name__ == '__main__':
    f = open('agent_config.yaml', 'w')
    f.write(yaml.dump(generate_agent_config(), default_flow_style=False))
    f.close()
