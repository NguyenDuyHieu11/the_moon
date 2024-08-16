# the_moon
version 0
virtual environment: "the_moon_venv"
.venv might be created while i'm in side "the_moon_venv"
__________________________________________________________________________________________________________________________________________________
temporary angular structure idea:
src/
  app/
    core/
      services/
        auth.service.ts
        data.service.ts
        // Other core services
      guards/
        auth.guard.ts
        // Other guards
      interceptors/
        error.interceptor.ts
        // Other interceptors
      models/
        // Shared models
    shared/
      components/
        // Reusable components
      directives/
        // Custom directives
      pipes/
        // Custom pipes
    features/
      auth/
        auth.module.ts
        login/
          login.component.ts
          login.component.html
          login.component.scss
        register/
          // ...
      dashboard/
        dashboard.module.ts
        dashboard.component.ts
        // ...
      // Other features
    environments/
      environment.ts
      environment.prod.ts
    assets/
      images/
      fonts/
      // Other assets
    styles.css
    index.html
    main.ts
__________________________________________________________________________________________________________________________________________________
Resources for the moon (apart from the official documents):

Angular Guards:
    https://github.com/angular-vietnam/100-days-of-angular/blob/master/Day030-router-guards-resolvers.md