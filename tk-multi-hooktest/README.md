# tk-multi-hooktest

This app is a very basic alteration of the ShotGrid default starter app with the intention
to demonstrate that the custom hooks do not provide stack trace when they error out
within maya. 

## Setup steps

1. Download app and place it somewhere locally on your machine
2. Add the following to your `app_locations.yml`
```yaml
apps.tk-multi-hooktest.location:
   type: path
   windows_path: path\to\the\app\tk-multi-hooktest
```

3. Create a `tk-multi-hooktest.yml` and add it to your env\includes\settings folder with
the following content. 

```yaml
includes:
- ../app_locations.yml

settings.tk-multi-hooktest:
#  hook_do_something: "{config}/tk-multi-hooktest/do_something.py"
  hook_do_something: "{self}/do_something.py"
  location: "@apps.tk-multi-hooktest.location"
```

4. Within your `tk-maya.yml` file add the following under `includes:`
```yaml
- ./tk-multi-hooktest.yml
```
And the following under your `settings.tk-maya.project:`
```yaml
tk-multi-hooktest: "@settings.tk-multi-hooktest"
```

The starter app should now be present when you launch Maya under the 
ShotGrid menu. When you launch it you will see two buttons in the ui.
The one will allow the hook to pass while the other should raise a tank error.