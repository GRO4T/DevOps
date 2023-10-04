from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: is_installed 

Module allows to test whether given program is installed.

version_added: "1.0.0"

options:
    name:
        description: Program name. 
        required: true
        type: str

author:
    - Damian Kolaska (GRO4T)
'''

EXAMPLES = r'''
- name: Check if Helm is installed
  is_installed:
    name: helm 
'''

RETURN = r'''
is_installed:
    description: Boolean telling whether the program is installed.
    type: bool
    returned: always
'''

from shutil import which

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        name=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        is_installed=False,
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    
    result["is_installed"] = which(module.params["name"]) is not None

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
