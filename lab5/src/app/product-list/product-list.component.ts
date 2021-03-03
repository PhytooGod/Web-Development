import { Component } from "@angular/core";
import { Input } from "@angular/core";
@Component({
  selector: "app-product-list",
  templateUrl: "./product-list.component.html",
  styleUrls: ["./product-list.component.css"]
})
export class ProductListComponent {
  @Input() product;
  @Input() category;
  constructor() {}

  ngOnInit() {}
  share(url: string) {
    window.open(url);
  }

  onNotify() {
    window.alert("You will be notified when the product goes on sale");
  }
}

/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
