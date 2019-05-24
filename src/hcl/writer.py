import json
from typing import List


class HclBase:
    """
    Baseclass to be used for objects which should be serialized as Stanza.
    The name of the Stanza is taken from the class-variable NAME
    """
    NAME = "HclBase"


def dumps(obj, intend=''):
    """

    :param obj:
    :param intend:
    :return:
    """
    content = ""
    if isinstance(obj, HclBase):
        # handle-class stuff
        # Append the Stanzas name to the content
        content += intend + obj.NAME
        attributes = _get_attributes(obj)
        attributes.remove('NAME')
        # If an HCL label (== Stanza Name) is set we append it as well
        if '_hcl_label' in attributes:
            hcl_label = getattr(obj, '_hcl_label')
            content += ' "' + hcl_label + '" '
            attributes.remove('_hcl_label')
        content += '{\n'
        intend += '\t'
        for attribute_name in attributes:
            attr_content = getattr(obj, attribute_name)
            if not isinstance(attr_content, HclBase):
                content += intend + attribute_name + ' = '
            content += dumps(attr_content, intend) + '\n'
        intend = intend[:-1]
        content += intend + '}'
        return content
    elif isinstance(obj, dict):
        content += '{\n'
        intend += '\t'
        for key, value in obj.items():
            content += intend + str(key) + ' = ' + str(value) + '\n'
        intend = intend[:-1]
        content += intend + '}'
        return content
    else:
        return json.dumps(obj)


def _get_attributes(obj) -> List[str]:
    """
    For internal usage. Returns a list containing the names of all variables used in the given obj
    :param obj: the obj the attributes (variables) are queried
    :return: list of variable names
    """
    attributes = []
    for maybe_attribute in dir(obj):
        if not maybe_attribute.startswith('__') and \
                not callable(getattr(obj, maybe_attribute)):
            attributes.append(maybe_attribute)
    return attributes
