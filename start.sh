#!/bin/bash

python generate_agent_config.py
newrelic-plugin-agent -c agent_config.yaml -f
