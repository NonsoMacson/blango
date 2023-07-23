class ClickButton extends React.Component{
  state={
    wasClicked: false
  }

  handleClicked(){
    this.setState(
      {wasClicked: true}
    )
  }

  render(){
    let buttonText

    if(this.state.wasClicked){
      buttonText="Clicked!"
    }else{
      buttonText= "Click me"
    }

    return React.createElement(
      'button',
      {
        className: 'btn btn-primary mt-2',
        onClick: ()=>{
          this.handleClicked()
        }
      }, buttonText
    )
  }
}


const domContainer=document.getElementById('react_root')

ReactDOM.render(React.createElement(ClickButton), domContainer)