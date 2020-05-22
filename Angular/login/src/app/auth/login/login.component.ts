import { element } from 'protractor';
import { FormControl, FormGroup} from '@angular/forms';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  loginForm = new FormGroup ({
    email : new FormControl(''),
    password : new FormControl('')
  });

  constructor() { }

  ngOnInit(): void {
  }
  onLogin (){
    console.log('Form->', this.loginForm.value)
  }

}
