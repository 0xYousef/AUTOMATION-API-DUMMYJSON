package automation.api.runners;

import automation.api.datafactory.UserProvider;

import com.automation.api.config.EnvironmentManager;
import com.automation.api.dto.UserForm;

public class UsersRunner {
    
    public static void main(String[] args) {

        EnvironmentManager manager = new EnvironmentManager("dev_v1");
        UsersSuits uSuits = new UsersSuits(manager);
        
        uSuits.setEnvirment("currentUser",UserProvider.createRandomUser());
        
        
        UserForm envUser = (UserForm) uSuits.getEnvirment("currentUser");
        System.out.println("Base URL: " + uSuits.url());
        System.out.println(envUser.toString());        
       
    }
}