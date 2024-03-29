
import splunk_ta_dynatrace_declare

from splunktaucclib.rest_handler.endpoint import (
    field,
    validator,
    RestModel,
    DataInputModel,
)
from splunktaucclib.rest_handler import admin_external, util
from splunk_aoblib.rest_migration import ConfigMigrationHandler

util.remove_http_proxy_env_vars()


fields = [
    field.RestField(
        'interval',
        required=True,
        encrypted=False,
        default=None,
        validator=validator.Pattern(
            regex=r"""^\-[1-9]\d*$|^\d*$""", 
        )
    ), 
    field.RestField(
        'index',
        required=True,
        encrypted=False,
        default='default',
        validator=validator.String(
            max_len=80, 
            min_len=1, 
        )
    ), 
    field.RestField(
        'dynatrace_tenant',
        required=True,
        encrypted=False,
        default='https://<tenant>.live.dynatrace.com',
        validator=validator.String(
            max_len=8192, 
            min_len=0, 
        )
    ), 
    field.RestField(
        'dynatrace_api_token',
        required=True,
        encrypted=True,
        default=None,
        validator=validator.String(
            max_len=8192, 
            min_len=0, 
        )
    ), 
    field.RestField(
        'dynatrace_collection_interval',
        required=True,
        encrypted=False,
        default='5mins',
        validator=None
    ), 
    field.RestField(
        'dynatrace_tags',
        required=False,
        encrypted=False,
        default='',
        validator=validator.String(
            max_len=8192, 
            min_len=0, 
        )
    ),
    field.RestField(
        'dynatrace_entities',
        required=False,
        encrypted=False,
        default='',
        validator=validator.String(
            max_len=8192, 
            min_len=0, 
        )
    ),
    field.RestField(
        'ssl_certificate_verification',
        required=False,
        encrypted=False,
        default=True,
        validator=None
    ), 

    field.RestField(
        'disabled',
        required=False,
        validator=None
    )

]
model = RestModel(fields, name=None)



endpoint = DataInputModel(
    'dynatrace_timeseries_metrics',
    model,
)


if __name__ == '__main__':
    admin_external.handle(
        endpoint,
        handler=ConfigMigrationHandler,
    )
