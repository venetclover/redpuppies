Rails.application.routes.draw do
  get 'house/index'

  resources :house do
    get 'autocomplete', :on => :collection
  end


  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root 'house#index'
end
