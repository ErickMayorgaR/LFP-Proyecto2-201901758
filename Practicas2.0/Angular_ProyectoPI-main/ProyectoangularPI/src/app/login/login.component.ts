import { Component, OnInit } from '@angular/core';
import {Router, ActivatedRoute, Params, RouterLink} from "@angular/router";
import { usuario } from '../modelos/usuario.model';
import { UsuarioService } from '../services/usuario.service';
import {NgbModal} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [UsuarioService] 
})
export class LoginComponent implements OnInit {
  public usuario: usuario
  public identity
  public status
  public error
  constructor(private router: Router, private _userService: UsuarioService, private modal: NgbModal) {
    this.usuario = new usuario("","","","","","",);
   }

  ngOnInit(): void {
    
  }

  openSM(contenido){
    this.modal.open(contenido,{size:'sm'});
  }

  login(){
    this._userService.login(this.usuario).subscribe(
      Response=>{
        this.identity = Response.usuario
        console.log("identity"+this.identity)
        if(!this.identity){
          this.status = 'wenas'
          console.log("logeado")
            
          this.router.navigate(['/principal'])
        }else{
          console.log("error")
          this.error = false
        }
      }),
      error => {
        var MensajeError = <any> error
        if(MensajeError != null){
          this.status = 'error';
          this.error = true;
        }
    }
    
  }
}
