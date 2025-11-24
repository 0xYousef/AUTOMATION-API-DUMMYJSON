package com.automation;


import com.automation.api.config.Environment;
import com.automation.api.config.EnvironmentManager;
import com.automation.api.dto.AuthForm;

public class Main {
    public static void main(String[] args) {
        EnvironmentManager env = new EnvironmentManager("prod_v1_");
        Environment postman = new Environment();
        
        postman.set("user", AuthForm.builder()

        .username("Yousef")
        .password("YousefPaas")
        .accessToken("AccessToken")
        .refreshToken("refreshTopken")
        .build());


        System.out.printf(
            "root: %s%nusername: %s - password: %s%n",
            env.getRoot(),
            env.getProperty("username"),
            env.getProperty("password")
        );
        System.out.println();
        AuthForm form = (AuthForm) postman.get("user");
        System.out.println(form.toString());
    }
}