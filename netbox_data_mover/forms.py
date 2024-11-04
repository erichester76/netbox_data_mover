from django import forms
from .models import DataMoverConfig, DataMoverDataSource


class DataMoverConfigForm(forms.ModelForm):
    class Meta:
        model = DataMoverConfig
        fields = ['name', 'description', 'schedule', 'source', 'source_endpoint', 'destination', 'destination_endpoint']
        widgets = {
            'source': forms.Select(attrs={'class': 'form-select'}),
            'source_endpoint': forms.Select(attrs={'class': 'form-select'}),
            'destination': forms.Select(attrs={'class': 'form-select'}),
            'destination_endpoint': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['source'].widget.attrs.update({'class': 'form-select d-inline-block col-md-6'})
        self.fields['source_endpoint'].widget.attrs.update({'class': 'form-select d-inline-block col-md-6'})
        self.fields['destination'].widget.attrs.update({'class': 'form-select d-inline-block col-md-6'})
        self.fields['destination_endpoint'].widget.attrs.update({'class': 'form-select d-inline-block col-md-6'})   
            
class DataMoverDataSourceForm(forms.ModelForm):
    class Meta:
        model = DataMoverDataSource
        fields = ['name', 'type', 'module', 'auth_method', 'auth_function', 'find_function', 'create_function', 'update_function', 'fetch_function', 'auth_args', 'base_urls']
