import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-aboutus',
  templateUrl: './aboutus.component.html',
  styleUrls: ['./aboutus.component.scss']
})
export class AboutusComponent implements OnInit {

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
