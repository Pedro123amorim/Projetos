package br.com.sistema.controller;

import br.com.sistema.model.User;
import br.com.sistema.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin(origins = "http://localhost:3000")
public class LoginController {

    @Autowired
    private UserRepository userRepository;

    @PostMapping("/api/login")
    public String login(@RequestBody User user) {
        // Busca o usuário no banco de dados
        User foundUser = userRepository.findByUsername(user.getUsername());

        // Verifica se o usuário existe e se a senha está correta
        if (foundUser != null && foundUser.getPassword().equals(user.getPassword())) {
            return "Login realizado com sucesso!";
        }
        return "Credenciais inválidas!";
    }
}
