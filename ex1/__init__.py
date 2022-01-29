def build_roles_tree(mapping):

	# создаём почти конечный результирующий список
    outputList = list()

	# проходим по входной структуре в соответствии с сортировкой
    for categoryId in mapping["categoryIdsSorted"]:
        tmpCategoryMap = dict()
        tmpCategoryMap["id"] = "category-" + categoryId
        tmpCategoryMap["text"] = mapping["categories"][categoryId]["name"]

        tmpItemsList = list() # наполняем список персонала категории
				# в соответствии со списком id ролей
        for roleId in mapping["categories"][categoryId]["roleIds"]:
            tmpItemsMap = dict()
            tmpItemsMap["id"] = roleId
            tmpItemsMap["text"] = mapping["roles"][roleId]["name"]
            tmpItemsList.append(tmpItemsMap)

        tmpCategoryMap["items"] = tmpItemsList
        outputList.append(tmpCategoryMap)

	# создаём окончательный результирующий словарь из одного элемента
    outputMap = dict()
    outputMap["categories"] = outputList
    return outputMap