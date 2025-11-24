package automation.api.datafactory;

import com.automation.api.dto.UserForm;
import com.github.javafaker.Faker;

public class UserProvider {
    private static final Faker faker = new Faker();
        
    private static UserForm generateBaseUser() {
        return UserForm.builder()
                .id(faker.number().numberBetween(1, 10000))
                .age(faker.number().numberBetween(18, 80))
                .username(faker.name().username())
                .password(faker.internet().password())
                .firstName(faker.name().firstName())
                .lastName(faker.name().lastName())
                .gender(faker.demographic().sex())
                .eyeColor(faker.options().option("Brown", "Blue", "Green"))
                .email(faker.internet().emailAddress())
                .image(faker.internet().image())
                .birthDate(faker.date().birthday().toString())
                .build();
    }
    
    public static UserForm createRandomUser() {
        return generateBaseUser();
    }
    
    public static UserForm createUserWithStrongPassword() {
        UserForm user = generateBaseUser();
        user.setPassword("StrongPwd123!");
        return user;
    }
}
