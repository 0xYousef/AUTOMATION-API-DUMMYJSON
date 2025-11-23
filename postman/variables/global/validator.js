function validator() {
    return {
        assertEqual: function(actual, expected, description = "Compare actual vs expected") {
            console.log(description, "| actual:", actual, "| expected:", expected);
            pm.test(description, function() {
                pm.expect(actual).to.eql(expected);
            });
        },

        assertNestedEqual: function(actualObj, path, expected, description = null) {
            const paths = path.split(".");
            let value = actualObj;
            for (let p of paths) {
                if (value && value.hasOwnProperty(p)) value = value[p];
                else { value = undefined; break; }
            }
            if (!description) description = `Compare nested path "${path}"`;
            console.log(description, "| actual:", value, "| expected:", expected);
            pm.test(description, function() {
                pm.expect(value).to.eql(expected);
            });
        },

        validateStatus: function(actualStatus, expectedStatus = null) {
            const statusMessages = {
                200: "OK", 201: "Created", 204: "No Content", 400: "Bad Request",
                401: "Unauthorized", 403: "Forbidden", 404: "Not Found",
                405: "Method Not Allowed", 409: "Conflict", 422: "Unprocessable Entity",
                500: "Internal Server Error", 502: "Bad Gateway", 503: "Service Unavailable"
            };
            const message = statusMessages[actualStatus] || "Unknown status code";
            console.log("Status:", actualStatus, "-", message);

            pm.test("Status validation", function() {
                if (expectedStatus !== null) pm.expect(actualStatus).to.eql(expectedStatus);
                else pm.expect(actualStatus).to.be.oneOf(Object.keys(statusMessages).map(Number));
            });
        },

        validateMessage: function(actualMessage, expectedMessage, messagePath = null) {
            let value = actualMessage;
            if (messagePath && actualMessage && typeof actualMessage === "object") {
                const paths = messagePath.split(".");
                for (let p of paths) {
                    if (value && value.hasOwnProperty(p)) value = value[p];
                    else { value = undefined; break; }
                }
            }
            console.log("Message validation | expected:", expectedMessage, "| actual:", value);
            pm.test("Message validation", function() {
                pm.expect(value).to.eql(expectedMessage);
            });
        },

        validateSchema: function(schema) {
            pm.test("JSON Schema validation", function() {
                pm.response.to.have.jsonSchema(schema);
            });
        },

        logResponse: function(response = null) {
            const resp = response || pm.response.json();
            console.log("Full response:", resp);
        }
    };
}