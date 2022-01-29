def build_roles_tree(mapping):
    roles = mapping['roles']
    categories = mapping['categories']
    category_ids_sorted = mapping['categoryIdsSorted']
    result_tree = {'categories': []}
    result_list = result_tree['categories']
    for categoryId in category_ids_sorted:
        category = categories[categoryId]
        role_ids = category['roleIds']
        result_category = {'id': 'category-' + categoryId, 'text': category['name'], 'items': []}
        items = result_category['items']
        for roleId in role_ids:
            items.append({'id': roleId, 'text': roles[roleId]['name']})
        result_list.append(result_category)
    return result_tree