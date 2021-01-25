from flask import request

from sample.models.filters.user_settings import UserSettings


def extract_query_params():
    return UserSettings(request.args.get('wasserError'),
                        request.args.get('varsFrom'),
                        request.args.get('varsUntil'),
                        request.args.get('varsStepSize'))
