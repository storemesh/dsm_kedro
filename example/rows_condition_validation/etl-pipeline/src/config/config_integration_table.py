#### Template ####
# integration_table =  {
#     "<your integration table 1>": None, 
#     '<your integration table 2>': None, 
#     '<your integration table 3>': {
#         'columns': {
#             'id': { 'data_type': 'string', 'is_required': True},
#             'title': { 'data_type': 'string', 'is_required': True},
#             'unit': { 'data_type': 'string', 'is_required': True},
#             'description': { 'data_type': 'string', 'is_required': False},
#             'unit_price': { 'data_type': 'float', 'is_required': True, 'validation_rule': [1]},
#         },
#         'pk_column': 'id',
#         'validation_rule': [1],   # for rows validation
#     }, 
# }

integration_table =  {
    'TM': {
        'columns': {
            'TR_NO': { 'data_type': 'int64', 'nullable': False, 'is_required': False},
            # 'TR_NO': { 'data_type': 'string', 'is_required': False},
            # 'TR_NO': { 'data_type': 'string', 'is_required': False},
            # 'TR_NO': { 'data_type': 'string', 'is_required': False},
            # 'unit_price': { 'data_type': 'float', 'is_required': True, 'validation_rule': [1]},
        },
        'pk_column': 'TR_NO',
        'validation_rule': [4],
        # 'validation_rule': [1],   # for rows validation
    },
    'PAT': {
        'columns': {
            'id': { 'data_type': 'string', 'is_required': True},
            'title': { 'data_type': 'string', 'is_required': True},
            'unit': { 'data_type': 'string', 'is_required': True},
            'description': { 'data_type': 'string', 'is_required': False},
            'unit_price': { 'data_type': 'float', 'is_required': True, 'validation_rule': [1]},
        },
        'pk_column': 'id',
        'validation_rule': [1],   # for rows validation
    }
}