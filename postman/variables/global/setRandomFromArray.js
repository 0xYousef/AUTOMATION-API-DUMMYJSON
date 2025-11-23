function setRandomFromArray(responseArray, fieldName, envVarName) {
    if (!Array.isArray(responseArray)) {
        console.log("Not an array:", responseArray);
        return null;
    }
    if (responseArray.length === 0) {
        console.log("No data found for " + envVarName);
        return null;
    }

    let index = Math.floor(Math.random() * responseArray.length);
    let item = responseArray[index];

    // If array of objects and fieldName exists
    let value = (fieldName && typeof item === "object") ? item[fieldName] : item;

    pm.environment.set(envVarName, value);
    console.log("Random " + envVarName + ": ", value);
    return value;
}