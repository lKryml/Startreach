export enum UsersTypes {
    NORMAL = 1,
    COMPANY,
    INVESTOR,
    GOVERMENT,
    NGO,
    EDUCATION,
    SYNDICATE,
}
let _usersTypesArray = [];
for (const i in UsersTypes) {
    if (parseInt(UsersTypes[i]) === UsersTypes.NORMAL) _usersTypesArray = [];
    console.log(i, UsersTypes[i])
    _usersTypesArray.push({
        id: parseInt(UsersTypes[i]),
        img: `../images/user_type_${UsersTypes[i]}`,
        title: `USERS.USER_TYPE_${UsersTypes[i]}`,
        description: `USERS.USER_TYPE_DESCRIPTION_${UsersTypes[i]}`
    });
}
export const UsersTypesArray = _usersTypesArray;