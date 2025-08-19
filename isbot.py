import re
import json

def load_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


crawler_user_agents = json.loads(load_file('crawler-user-agents.json'))
# custom_user_agents = json.loads(load_file('custom.json'))

# user agent strings for bots
user_agents_raw = load_file('user-agents-bots.txt')
user_agents = user_agents_raw.splitlines()


matchers = []


for definition in crawler_user_agents:
    pattern = definition['pattern']
    try:
        matchers.append(re.compile(pattern, re.IGNORECASE))
    except re.error as e:
        raise ValueError(f"Invalid regex pattern: {pattern}") from e

# for definition in custom_user_agents:
#     pattern = definition['pattern']
#     try:
#         matchers.append(re.compile(pattern, re.IGNORECASE))
#     except re.error as e:
#         raise ValueError(f"Invalid regex pattern: {pattern}") from e

def check_regex(user_agent):
    for matcher in matchers:
        if matcher.search(user_agent):
            return True
    return False

def check_list(user_agent):
    return user_agent in user_agents


def check(user_agent):
    if check_list(user_agent):
        return True
    return check_regex(user_agent)


if __name__ == "__main__":
    user_agent1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    user_agent2 = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0"
    if check(user_agent2):
        print("User-agent is recognized as a bot!")
    else:
        print("User-agent is not recognized as a bot.")
