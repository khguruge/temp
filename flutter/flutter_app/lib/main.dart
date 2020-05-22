import 'package:flutter/material.dart';

main(){
  runApp(MyaApp());
}

  class MyaApp extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.blueGrey,
        appBar: AppBar(
          title : Text("hello Pro"),
          backgroundColor: Colors.blueGrey[900],
        ),

          body: Center(
            child: Image(
              image: NetworkImage('https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60'),
            ),
          )
      )
  );
  }
}