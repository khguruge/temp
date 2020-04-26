import { Component, OnInit } from '@angular/core';

export interface Employee {
  id:string;
  name:string;
  email:string;
  password:string;
}


@Component({
  selector: 'app-aboutus',
  templateUrl: './aboutus.component.html',
  styleUrls: ['./aboutus.component.scss']
})
export class AboutusComponent implements OnInit {

    employees : Employee[] = [
      {id :'001', name : 'Kasun', email : 'khguruge@gmail.com', password : '123'},
      {id :'002', name : 'Harshana', email : 'guruge@gmail.com', password : '123'},
      {id :'003', name : 'Guruge', email : 'kh@gmail.com', password : '123'}
    ]

  constructor() { }

  ngOnInit(): void {
  }
  show(){
    alert('Helloooooooo Kasun');
    console.log('machan');
  }
  show02(){
    alert('Helloooooooo Kasun Prooo');
  }

}
