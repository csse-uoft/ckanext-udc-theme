from ckan.types import Schema
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
import json
import os


"""
See https://docs.ckan.org/en/latest/theming/templates.html
See https://docs.ckan.org/en/latest/extensions/adding-custom-fields.html
"""


class UdcPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.ITemplateHelpers)

    # Load JSON config
    config_file = open(os.path.join(os.path.dirname(__file__), "config.json"))
    config = json.load(config_file)

    all_fields = []
    for level in config:
        for field in level["fields"]:
            if field.get("name"):
                all_fields.append(field["name"])

    def update_config(self, config_):
        tk.add_template_directory(config_, 'templates')
        tk.add_public_directory(config_, 'public')
        tk.add_resource('assets', 'udc')

    def _modify_package_schema(self, schema: Schema) -> Schema:
        # our custom field
        for field in self.all_fields:
            schema.update({
                field: [tk.get_validator('ignore_missing'),
                        tk.get_converter('convert_to_extras')],
            })

        return schema

    def create_package_schema(self) -> Schema:
        # let's grab the default schema in our plugin
        schema: Schema = super(UdcPlugin, self).create_package_schema()
        return self._modify_package_schema(schema)

    def update_package_schema(self) -> Schema:
        schema: Schema = super(UdcPlugin, self).update_package_schema()
        # our custom field
        return self._modify_package_schema(schema)

    def show_package_schema(self) -> Schema:
        schema: Schema = super(UdcPlugin, self).show_package_schema()
        for field in self.all_fields:
            schema.update({
                field: [tk.get_converter('convert_from_extras'),
                        tk.get_validator('ignore_missing')],
            })

        return schema

    def get_helpers(self):
        return {"config": self.config}

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self): # -> list[str]
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
